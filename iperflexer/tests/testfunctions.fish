function twparsers
    cd ../
    tangleweave iperfparser.pnw
    tangleweave sumparser.pnw
    tangleweave unitconverter.pnw
    cd tests/steps
end

function transferfeature
    twparsers
    tangleweave transferfeature.pnw
    cd ../
    behave features/transfer.feature
end

function casterfeature
    twparsers
    tangleweave casterfeature.pnw
    cd ../
    behave features/caster.feature
end

function lastlinebandwidth
    twparsers
    tangleweave lastlinebandwidth.pnw
    cd ../
    behave features/lastlinebandwidth.feature
end    

function binaryunitconverter
    twparsers
    tangleweave binaryunitconverter.pnw
    cd ../
    behave features/binaryunitconverter.feature
end

function iperfbinaryunitconverter
    twparsers
    tangleweave iperfbinaryconverter.pnw
    cd ../
    behave features/iperfbinaryconverter.feature
end

function decimalunitconverter
    twparsers
    tangleweave decimalunitconverter.pnw
    cd ../
    behave features/decimalunitconverter.feature
end

function testall
    twparsers
    for name in (ls | grep ".*pnw" | grep -v index.pnw)
         tangleweave $name
    end
    cd ../
    behave features/
end
