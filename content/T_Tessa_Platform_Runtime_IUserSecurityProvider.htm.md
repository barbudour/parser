# IUserSecurityProvider - интерфейс
Объект, управляющий хранением объекта с настройками безопасности сотрудника
[UserSecurityObject](T_Tessa_Platform_Runtime_UserSecurityObject.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IUserSecurityProvider
VB __Копировать
     Public Interface IUserSecurityProvider
C++ __Копировать
     public interface class IUserSecurityProvider
F# __Копировать
     type IUserSecurityProvider = interface end
##  __Методы
[GetSecurityObjectAsync](M_Tessa_Platform_Runtime_IUserSecurityProvider_GetSecurityObjectAsync.htm)|
Возвращает объект с настройками безопасности для сотрудника с заданным
идентификатором. Если сотрудник отсутствует или для него ещё не указаны
настройки безопасности, то возвращает объект с параметрами по умолчанию. Не
возвращает null. В реализации по умолчанию метод не обеспечивает
транзакционности и блокировки на настройки безопасности для сотрудника, об
этом должен заботиться вышележащий код.  
---|---  
[StoreSecurityObjectAsync](M_Tessa_Platform_Runtime_IUserSecurityProvider_StoreSecurityObjectAsync.htm)|
Сохраняет объект с настройками безопасности для сотрудника с заданным
идентификатором. Если сотрудник отсутствует, то метод не выполняет действий. В
реализации по умолчанию метод не обеспечивает транзакционности и блокировки на
настройки безопасности для сотрудника, об этом должен заботиться вышележащий
код.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
