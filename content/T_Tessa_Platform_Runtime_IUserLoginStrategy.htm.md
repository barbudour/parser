# IUserLoginStrategy - интерфейс
Объект, определяющий правила блокировки сотрудника после успешного или
неуспешного логина / изменения пароля.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IUserLoginStrategy
VB __Копировать
     Public Interface IUserLoginStrategy
C++ __Копировать
     public interface class IUserLoginStrategy
F# __Копировать
     type IUserLoginStrategy = interface end
##  __Методы
[BlockUserIfRequiredAndGetExceptionAsync](M_Tessa_Platform_Runtime_IUserLoginStrategy_BlockUserIfRequiredAndGetExceptionAsync.htm)|
Метод вызывается при неверно введённом пароле. Блокирует пользователя, если
этого требуют настройки, и возвращает исключение с кодом ошибки в случае
блокировки пользователя.  
---|---  
[UpdateSecurityOnSuccessfulLoginAsync](M_Tessa_Platform_Runtime_IUserLoginStrategy_UpdateSecurityOnSuccessfulLoginAsync.htm)|
Метод вызывается после корректно введённого пароля. Обнуляет счётчики
неудачных попыток ввода.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
