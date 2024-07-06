describe('suite', function() {

  it('spec', function() {
      // setup
      jasmine.clock().install();

      var spy = jasmine.createSpy();

      // exercise
      setTimeout(function() {
          spy();
      }, 100);

      jasmine.clock().tick(101); // 時は加速する

      // verify
      expect(spy).toHaveBeenCalled();

      // teardown
      jasmine.clock().uninstall();
  });
});
