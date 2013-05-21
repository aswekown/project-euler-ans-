(loop for i 
        below 1000
        when (or (zerop (rem i 3)) (zerop (rem i 5)))
        sum i)
