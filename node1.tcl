set ns [new Simulator]

set nt [open out.tr w]
$ns trace-all $nt

set nf [open out.nam w]
$ns namtrace-all $nf

set n0 [$ns node]
set n1 [$ns node]

$ns duplex-link $n0 $n1 3Mb 3ms DropTrail

set udp0 [new Agent/UDP]
$ns attach-agent $n0 $udp0

set cbr0 [new Application/Traffic/CBR]
$cbr0 attach-agent $udp0

se null0 [new Agent/Null]
$ns attach-agent $n1 $null0
$ns connect $udp0 $null0

proc finish {} {
        global ns nt nf
        $ns flush-trace
        close $nt
        close $nf
        exec nam out.nam &
        exit 0
}

$ns at 1.0 "$cbr0 start"
$ns at 8.0 "$cbr0 stop"

$ns at 5.0 "finish"
$ns run
