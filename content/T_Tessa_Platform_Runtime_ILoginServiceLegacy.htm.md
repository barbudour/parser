# ILoginServiceLegacy - интерфейс
Сервис, обеспечивающий аутентификацию пользователей.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [ServiceContractAttribute(Name = "ILoginService")]
    [SessionServiceAttribute("service address is specified in LoginServiceLegacyProxy", 
    	TransferMode.Buffered)]
    public interface ILoginServiceLegacy
VB __Копировать
    <ServiceContractAttribute(Name := "ILoginService")>
    <SessionServiceAttribute("service address is specified in LoginServiceLegacyProxy", 
    	TransferMode.Buffered)>
    Public Interface ILoginServiceLegacy
C++ __Копировать
    [ServiceContractAttribute(Name = L"ILoginService")]
    [SessionServiceAttribute(L"service address is specified in LoginServiceLegacyProxy", 
    	TransferMode::Buffered)]
    public interface class ILoginServiceLegacy
F# __Копировать
     [<ServiceContractAttribute(Name = "ILoginService")>]
    [<SessionServiceAttribute("service address is specified in LoginServiceLegacyProxy", 
    	TransferMode.Buffered)>]
    type ILoginServiceLegacy = interface end
##  __Методы
[OpenSession](M_Tessa_Platform_Runtime_ILoginServiceLegacy_OpenSession.htm)|
Выполняет аутентификацию пользователя, используя анонимную аутентификацию по
учётной записи Windows и по заданным параметрам логин/пароль/доменное имя, или
используя аутентификацию для пользователя Tessa. Открывает сессию и возвращает
её токен [Tessa.Platform.Runtime.SessionToken], сериализованный в формате XML.  
---|---  
[OpenSessionWindowsAuth](M_Tessa_Platform_Runtime_ILoginServiceLegacy_OpenSessionWindowsAuth.htm)|
Выполняет аутентификацию пользователя по учётной записи Windows. Открывает
сессию и возвращает её токен [Tessa.Platform.Runtime.SessionToken],
сериализованный в формате XML.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
