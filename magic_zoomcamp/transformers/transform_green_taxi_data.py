if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data = data[data['passenger_count'] > 0]
    data = data[data['trip_distance'] > 0]

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data['lpep_dropoff_date'] = data['lpep_dropoff_datetime'].dt.date

    data = data.rename(columns={
        'VendorID': 'vendor_id',
        'passenger_count': 'passenger_count',
        'trip_distance': 'trip_distance',
        'RatecodeID': 'rate_code_id',
        'store_and_fwd_flag': 'store_and_fwd_flag',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id',
        'payment_type': 'payment_type',
        'fare_amount': 'fare_amount',
        'extra': 'extra',
        'mta_tax': 'mta_tax',
        'tip_amount': 'tip_amount',
        'tolls_amount': 'tolls_amount',
        'improvement_surcharge': 'improvement_surcharge',
        'total_amount': 'total_amount',
        'congestion_surcharge': 'congestion_surcharge'
    })

    # Specify your transformation logic here

    return data


@test
def test_output0(output,*args) -> None:
    assert output is not None, 'The output is undefined'

@test
def test_output1(output, *args) -> None:   
    # Assertion for passenger_count
    assert (output['passenger_count'] > 0).all(), "passenger_count contains non-positive values"
@test
def test_output2(output, *args) -> None:   
    # Assertion for trip_distance
    assert (output['trip_distance'] > 0).all(), "trip_distance contains non-positive values"

@test
def test_output3(output, *args) -> None:
     assert output['vendor_id'].isin(output['vendor_id']).all(), "vendor_id contains invalid values"