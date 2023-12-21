# IClientInitializationExtension - интерфейс
Расширение для инициализации приложений со стороны клиента.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IClientInitializationExtension : IExtension
VB __Копировать
     Public Interface IClientInitializationExtension
    	Inherits IExtension
C++ __Копировать
     public interface class IClientInitializationExtension : IExtension
F# __Копировать
     type IClientInitializationExtension = 
        interface
            interface IExtension
        end
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[AfterRequest](M_Tessa_Platform_Initialization_IClientInitializationExtension_AfterRequest.htm)|
Выполняет инициализацию приложения со стороны клиента после отправки запроса
на сервер, в т.ч. добавление обработчиков инициализации.  
---|---  
[AfterRequestFinally](M_Tessa_Platform_Initialization_IClientInitializationExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после инициализации
приложения со стороны клиента как при успешном, так и при неудачном
результате. Необработанные исключения не прерывают выполнение цепочки
расширений.  
[BeforeRequest](M_Tessa_Platform_Initialization_IClientInitializationExtension_BeforeRequest.htm)|
Выполняет инициализацию приложения со стороны клиента перед отправкой запроса
на сервер, в т.ч. добавление обработчиков инициализации.  
## __См. также
#### Ссылки
[Tessa.Platform.Initialization - пространство
имён](N_Tessa_Platform_Initialization.htm)
