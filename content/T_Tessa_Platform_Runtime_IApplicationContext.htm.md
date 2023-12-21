# IApplicationContext - интерфейс
Контекст, связанный с запуском или завершением приложения.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationContext
VB __Копировать
     Public Interface IApplicationContext
C++ __Копировать
     public interface class IApplicationContext
F# __Копировать
     type IApplicationContext = interface end
##  __Свойства
[Application](P_Tessa_Platform_Runtime_IApplicationContext_Application.htm)|
Приложение, с которым связан контекст.  
---|---  
[ExecuteCommandFunc](P_Tessa_Platform_Runtime_IApplicationContext_ExecuteCommandFunc.htm)|
Функция, выполняющая нестандартную команду, полученную из командной строки,
или null, если функция не задана.  
[Info](P_Tessa_Platform_Runtime_IApplicationContext_Info.htm)| Дополнительная
информация, связанная с приложением.  
[LaunchParameters](P_Tessa_Platform_Runtime_IApplicationContext_LaunchParameters.htm)|
Параметры запуска приложения, которые были указаны при запуске.  
[LaunchResult](P_Tessa_Platform_Runtime_IApplicationContext_LaunchResult.htm)|
Результат запуска приложения или null, если приложение ещё не было запущено.  
[Parameters](P_Tessa_Platform_Runtime_IApplicationContext_Parameters.htm)|
Параметры запуска приложения, которые были определены в процессе запуска.  
[ParseCommandFunc](P_Tessa_Platform_Runtime_IApplicationContext_ParseCommandFunc.htm)|
Функция, выполняющая разбора нестандартного аргумента командной строки, или
null, если функция не задана.  
[ValidationResult](P_Tessa_Platform_Runtime_IApplicationContext_ValidationResult.htm)|
Сообщения валидации.  
##  __Методы
[ResetValidationResult](M_Tessa_Platform_Runtime_IApplicationContext_ResetValidationResult.htm)|
Очищает результат валидации [Tessa.Platform.Runtime.IApplicationContext], т.о.
его можно будет заполнять новыми сообщениями.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
