# Machine Assignment 4 - Clever Mole 
## Purpose
This program demonstrates:

- How finite differences can approximate derivatives
- The effects of **step size h** on approximation accuracy
- How **floating-point precision limits** affect results as `h → 0`
- The trade-off between truncation error and round-off error

The program uses `f(x)=sin(x)` as the test function, with known derivate `f'(x)=cos(x)`, to analyze the forward difference approximation: `f'(x) ~= [f(x+h) - f(x)] / h`

---

## Usage
No inputs are required — all values are hardcoded.
```bash
python finite_difference.py
```

#### Requirements
This program uses matplotlib to ggenerate the log-log plot, must install it prior to running:
`pip install matplotlib`

#### Example Output
```bash
Cleve-Moler epsilon: 0.00000000000000022204
Square root of epsilon: 0.00000001490116119385

|  h  |       x       | Approx. f(x)  |  Known f(x)   |  Abs. Error   |
|:---:|---------------|---------------|---------------|---------------|
|2^-01|     1.00000000|     0.31204800|     0.54030231|     0.22825430|
|2^-02|     1.00000000|     0.43005454|     0.54030231|     0.11024777|
|2^-03|     1.00000000|     0.48637287|     0.54030231|     0.05392943|
|2^-04|     1.00000000|     0.51366321|     0.54030231|     0.02663910|
|2^-05|     1.00000000|     0.52706746|     0.54030231|     0.01323485|
|2^-06|     1.00000000|     0.53370646|     0.54030231|     0.00659584|
|2^-07|     1.00000000|     0.53700983|     0.54030231|     0.00329248|
|2^-08|     1.00000000|     0.53865744|     0.54030231|     0.00164487|
|2^-09|     1.00000000|     0.53948021|     0.54030231|     0.00082209|
|2^-10|     1.00000000|     0.53989135|     0.54030231|     0.00041096|
|2^-11|     1.00000000|     0.54009685|     0.54030231|     0.00020546|
|2^-12|     1.00000000|     0.54019958|     0.54030231|     0.00010272|
|2^-13|     1.00000000|     0.54025095|     0.54030231|     0.00005136|
|2^-14|     1.00000000|     0.54027663|     0.54030231|     0.00002568|
|2^-15|     1.00000000|     0.54028947|     0.54030231|     0.00001284|
|2^-16|     1.00000000|     0.54029589|     0.54030231|     0.00000642|
|2^-17|     1.00000000|     0.54029910|     0.54030231|     0.00000321|
|2^-18|     1.00000000|     0.54030070|     0.54030231|     0.00000160|
|2^-19|     1.00000000|     0.54030150|     0.54030231|     0.00000080|
|2^-20|     1.00000000|     0.54030190|     0.54030231|     0.00000040|
|2^-21|     1.00000000|     0.54030211|     0.54030231|     0.00000020|
|2^-22|     1.00000000|     0.54030221|     0.54030231|     0.00000010|
|2^-23|     1.00000000|     0.54030226|     0.54030231|     0.00000005|
|2^-24|     1.00000000|     0.54030228|     0.54030231|     0.00000003|
|2^-25|     1.00000000|     0.54030229|     0.54030231|     0.00000001|
|2^-26|     1.00000000|     0.54030230|     0.54030231|     0.00000001|
|2^-27|     1.00000000|     0.54030231|     0.54030231|     0.00000000|
|2^-28|     1.00000000|     0.54030231|     0.54030231|     0.00000000|
|2^-29|     1.00000000|     0.54030228|     0.54030231|     0.00000003|
|2^-30|     1.00000000|     0.54030228|     0.54030231|     0.00000003|

Minimum Absolute Error: 0.00000000054551074768
Compare to sqrt(eps): 0.00000001490116119385
```

The program also generates a log-log plot [error_plot.png](./error_plot.png) showing the characteristic U-shaped error curve.

## Testing
```bash
python3 test_finite_difference.py
```