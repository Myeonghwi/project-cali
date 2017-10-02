var elec_area = [
      { y: 'Jan', a: 50, b: 90},
      { y: 'Feb', a: 65,  b: 75},
      { y: 'Mar', a: 50,  b: 50},
      { y: 'Apr', a: 75,  b: 60},
      { y: 'May', a: 80,  b: 65},
      { y: 'Jun', a: 90,  b: 70},
      { y: 'Jul', a: 100, b: 75},
      { y: 'Aug', a: 115, b: 75},
      { y: 'Sep', a: 120, b: 85},
      { y: 'Oct', a: 145, b: 85},
      { y: 'Nov', a: 160, b: 95},
      { y: 'Dec', a: 160, b: 95}
    ],
    config_elec_area = {
      data: elec_area,
      xkey: 'y',
      ykeys: ['a', 'b'],
      labels: ['실제 전기 사용량', '보정 전기 사용량'],
      fillOpacity: 0.3,
      hideHover: 'auto',
      behaveLikeLine: true,
      resize: true,
      pointFillColors:['#ffffff'],
      pointStrokeColors: ['black'],
      lineColors:['gray','blue'],
      parseTime: false
      };

var gas_area = [
      { y: 'Jan', a: 50, b: 90},
      { y: 'Feb', a: 65,  b: 75},
      { y: 'Mar', a: 50,  b: 50},
      { y: 'Apr', a: 75,  b: 60},
      { y: 'May', a: 80,  b: 65},
      { y: 'Jun', a: 90,  b: 70},
      { y: 'Jul', a: 100, b: 75},
      { y: 'Aug', a: 115, b: 75},
      { y: 'Sep', a: 120, b: 85},
      { y: 'Oct', a: 145, b: 85},
      { y: 'Nov', a: 160, b: 95},
      { y: 'Dec', a: 160, b: 95}
    ],
    config_gas_area = {
      data: gas_area,
      xkey: 'y',
      ykeys: ['a', 'b'],
      labels: ['실제 가스 사용량', '보정 가스 사용량'],
      fillOpacity: 0.3,
      hideHover: 'auto',
      behaveLikeLine: true,
      resize: true,
      pointFillColors:['#ffffff'],
      pointStrokeColors: ['black'],
      lineColors:['gray','red'],
      parseTime: false
  };
config_elec_area.element = 'elec-area-chart';
Morris.Area(config_elec_area);
config_gas_area.element = 'gas-area-chart';
Morris.Area(config_gas_area);

//Morris.Bar(config)