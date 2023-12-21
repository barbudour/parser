# ILoginProvider - интерфейс
Объект, обеспечивающий получение информации по логину/паролю. Например, объект
может запросить параметры у пользователя, показав ему диалог. Объект
зарегистрирован на клиенте.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ILoginProvider
VB __Копировать
     Public Interface ILoginProvider
C++ __Копировать
     public interface class ILoginProvider
F# __Копировать
     type ILoginProvider = interface end
##  __Методы
[GetLoginParametersAsync](M_Tessa_Platform_Runtime_ILoginProvider_GetLoginParametersAsync.htm)|
Возвращает логин и пароль, используемые для входа в систему. Вход считается
отменённым, если логин или пароль равны null или пустой строке.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
