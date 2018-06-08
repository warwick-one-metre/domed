RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

all:
	mkdir -p build
	${RPMBUILD} -ba onemetre-dome-server.spec
	${RPMBUILD} -ba onemetre-dome-client.spec
	${RPMBUILD} -ba rasa-dome-server.spec
	${RPMBUILD} -ba python34-warwick-w1m-dome.spec
	mv build/noarch/*.rpm .
	rm -rf build

