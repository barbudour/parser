# ISessionTokenHolder - интерфейс
Объект, содержащий токен, связанный с текущей сессией. Используется на клиенте
для передачи данных между запросами.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISessionTokenHolder
VB __Копировать
     Public Interface ISessionTokenHolder
C++ __Копировать
     public interface class ISessionTokenHolder
F# __Копировать
     type ISessionTokenHolder = interface end
##  __Свойства
[SessionToken](P_Tessa_Platform_Runtime_ISessionTokenHolder_SessionToken.htm)|
Токен для текущей сессии или null, если токен ещё не был задан.  
---|---  
## __Методы
[SetSessionTokenAsync](M_Tessa_Platform_Runtime_ISessionTokenHolder_SetSessionTokenAsync.htm)|
Устанавливает токен для текущей сессии. Может быть равен null, если считается,
что токен ещё не был задан.  
---|---  
## __События
[SessionTokenChanged](E_Tessa_Platform_Runtime_ISessionTokenHolder_SessionTokenChanged.htm)|
Событие, происходящее при изменении токена для текущей сессии.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
