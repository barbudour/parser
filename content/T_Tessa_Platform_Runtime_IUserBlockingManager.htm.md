# IUserBlockingManager - интерфейс
Объект, управляющий установкой и снятием блокировки сотрудника.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IUserBlockingManager
VB __Копировать
     Public Interface IUserBlockingManager
C++ __Копировать
     public interface class IUserBlockingManager
F# __Копировать
     type IUserBlockingManager = interface end
##  __Методы
[BlockUserAsync](M_Tessa_Platform_Runtime_IUserBlockingManager_BlockUserAsync.htm)|
Устанавливает блокировку входа для пользователя с заданными параметрами.
Возвращает признак того, что сотрудник существует и блокировка установлена.  
---|---  
[UnblockUserAsync](M_Tessa_Platform_Runtime_IUserBlockingManager_UnblockUserAsync.htm)|
Снимает блокировку входа для пользователя с заданными параметрами. Обычно
используется при окончании срока временной блокировки. Возвращает признак
того, что сотрудник существует и блокировка снята.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
