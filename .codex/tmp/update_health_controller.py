from pathlib import Path
p = Path(r'G:\AI-law-creater\backend\src\main\java\com\laborlaw\ragkbdemo\controller\HealthController.java')
p.write_text('''package com.laborlaw.ragkbdemo.controller;

import com.laborlaw.ragkbdemo.vo.ApiResponse;
import com.laborlaw.ragkbdemo.vo.HealthVO;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
public class HealthController {

    @GetMapping("/health")
    public ApiResponse<HealthVO> health() {
        return ApiResponse.success(new HealthVO("ok"));
    }
}
''', encoding='utf-8')
print('updated', p)
