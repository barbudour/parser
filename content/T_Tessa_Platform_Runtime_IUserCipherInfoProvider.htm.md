# IUserCipherInfoProvider - интерфейс
Объект, управляющий хранением объекта с настройками по шифрованию клиентских
данных в папках пользователя
[UserCipherInfoObject](T_Tessa_Platform_Runtime_UserCipherInfoObject.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IUserCipherInfoProvider
VB __Копировать
     Public Interface IUserCipherInfoProvider
C++ __Копировать
     public interface class IUserCipherInfoProvider
F# __Копировать
     type IUserCipherInfoProvider = interface end
##  __Методы
[GetCipherInfoObjectAsync](M_Tessa_Platform_Runtime_IUserCipherInfoProvider_GetCipherInfoObjectAsync.htm)|
Возвращает объект с настройками по шифрованию клиентских данных для сотрудника
с заданным идентификатором. Если сотрудник отсутствует или для него ещё не
указаны настройки по шифрованию клиентских данных, то возвращает объект с
параметрами по умолчанию. Не возвращает null. В реализации по умолчанию метод
не обеспечивает транзакционности и блокировки на настройки по шифрованию
клиентских данных для сотрудника, об этом должен заботиться вышележащий код.  
---|---  
[StoreCipherInfoObjectAsync](M_Tessa_Platform_Runtime_IUserCipherInfoProvider_StoreCipherInfoObjectAsync.htm)|
Сохраняет объект с настройками по шифрованию клиентских данных для сотрудника
с заданным идентификатором. Если сотрудник отсутствует, то метод не выполняет
действий. В реализации по умолчанию метод не обеспечивает транзакционности и
блокировки на настройки по шифрованию клиентских данных для сотрудника, об
этом должен заботиться вышележащий код.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
