# IServerInitializationExtension - интерфейс
Расширение для инициализации приложений со стороны сервера.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IServerInitializationExtension : IExtension
VB __Копировать
     Public Interface IServerInitializationExtension
    	Inherits IExtension
C++ __Копировать
     public interface class IServerInitializationExtension : IExtension
F# __Копировать
     type IServerInitializationExtension = 
        interface
            interface IExtension
        end
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[AfterRequest](M_Tessa_Platform_Initialization_IServerInitializationExtension_AfterRequest.htm)|
Выполняет инициализацию приложения со стороны сервера после формирования
базового ответа от сервера, в т.ч. добавление обработчиков инициализации.  
---|---  
[AfterRequestFinally](M_Tessa_Platform_Initialization_IServerInitializationExtension_AfterRequestFinally.htm)|
Действие, выполняемое при возникновении исключения или после инициализации
приложения со стороны сервера как при успешном, так и при неудачном
результате. Необработанные исключения не прерывают выполнение цепочки
расширений.  
[BeforeRequest](M_Tessa_Platform_Initialization_IServerInitializationExtension_BeforeRequest.htm)|
Выполняет инициализацию приложения со стороны сервера перед формированием
базового ответа от сервера, в т.ч. добавление обработчиков инициализации.  
## __См. также
#### Ссылки
[Tessa.Platform.Initialization - пространство
имён](N_Tessa_Platform_Initialization.htm)
