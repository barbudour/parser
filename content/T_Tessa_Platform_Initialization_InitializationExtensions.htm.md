# InitializationExtensions - класс
Методы-расширения для пространства имён Tessa.Platform.Initialization.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class InitializationExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class InitializationExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class InitializationExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type InitializationExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ InitializationExtensions
##  __Методы
[RegisterClientInitializationExtensionTypes](M_Tessa_Platform_Initialization_InitializationExtensions_RegisterClientInitializationExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений для API инициализации на
клиенте.  
---|---  
[RegisterInitializationOnClient](M_Tessa_Platform_Initialization_InitializationExtensions_RegisterInitializationOnClient.htm)|
Выполняет регистрацию в контейнере Unity для API инициализации со стороны
клиента.  
[RegisterInitializationOnServer](M_Tessa_Platform_Initialization_InitializationExtensions_RegisterInitializationOnServer.htm)|
Выполняет регистрацию в контейнере Unity для API инициализации со стороны
сервера.  
[RegisterInitializationTraceListenersOnClient](M_Tessa_Platform_Initialization_InitializationExtensions_RegisterInitializationTraceListenersOnClient.htm)|
Выполняет регистрацию объектов, отслеживающих события, происходящие при
выполнении расширений на инициализацию приложения со стороны клиента, и
записывающие результат выполнения в
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)
как информационное сообщение. Это полезно при отладке расширений, но сильно
нагружает любое взаимодействие с плитками, поэтому рекомендуется не выполнять
такую регистрацию в среде, с которой работают конечные пользователи.  
[RegisterInitializationTraceListenersOnServer](M_Tessa_Platform_Initialization_InitializationExtensions_RegisterInitializationTraceListenersOnServer.htm)|
Выполняет регистрацию объектов, отслеживающих события, происходящие при
выполнении расширений на инициализацию приложения со стороны сервера, и
записывающие результат выполнения в
[ValidationResult](P_Tessa_Extensions_ITraceableExtensionContext_ValidationResult.htm)
как информационное сообщение. Это полезно при отладке расширений, но сильно
нагружает любое взаимодействие с плитками, поэтому рекомендуется не выполнять
такую регистрацию в среде, с которой работают конечные пользователи.  
[RegisterServerInitializationExtensionTypes](M_Tessa_Platform_Initialization_InitializationExtensions_RegisterServerInitializationExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений для API инициализации на
сервере.  
[RegisterWorkplaceInitializationRule<T>](M_Tessa_Platform_Initialization_InitializationExtensions_RegisterWorkplaceInitializationRule__1.htm)|
Выполняет регистрацию правила инициализации рабочих мест. Обычно правило
наследуется от базового класса
[WorkplaceInitializationRule](T_Tessa_Platform_Initialization_WorkplaceInitializationRule.htm).  
[RemoveInitializationTraceListenersOnClient](M_Tessa_Platform_Initialization_InitializationExtensions_RemoveInitializationTraceListenersOnClient.htm)|
Удаляет объекты, зарегистрированные методом
[RegisterInitializationTraceListenersOnClient(IExtensionContainer,
ExtensionTraceListenerType,
Nullable<Int64>)](M_Tessa_Platform_Initialization_InitializationExtensions_RegisterInitializationTraceListenersOnClient.htm).
Частая регистрация с последующим удалением объектов значительно нагружает
память и CPU.  
[RemoveInitializationTraceListenersOnServer](M_Tessa_Platform_Initialization_InitializationExtensions_RemoveInitializationTraceListenersOnServer.htm)|
Удаляет объекты, зарегистрированные методом
[RegisterInitializationTraceListenersOnServer(IExtensionContainer,
ExtensionTraceListenerType,
Nullable<Int64>)](M_Tessa_Platform_Initialization_InitializationExtensions_RegisterInitializationTraceListenersOnServer.htm).
Частая регистрация с последующим удалением объектов значительно нагружает
память и CPU.  
[SetConfigurationInfo](M_Tessa_Platform_Initialization_InitializationExtensions_SetConfigurationInfo.htm)|
Сохраняет сериализованную информацию по текущей версии конфигурации в объекте
[InitializationResponse](T_Tessa_Platform_Initialization_InitializationResponse.htm).  
[SetTypeIDListToLoad](M_Tessa_Platform_Initialization_InitializationExtensions_SetTypeIDListToLoad.htm)|
Устанавливает список идентификаторов типов карточек, которые должны
загружаться при инициализации.  
[TryGetConfigurationInfo](M_Tessa_Platform_Initialization_InitializationExtensions_TryGetConfigurationInfo.htm)|
Возвращает информацию по текущей версии конфигурации, которая сериализована в
заданном объекте
[InitializationResponse](T_Tessa_Platform_Initialization_InitializationResponse.htm),
или null, если информация недоступна.  
[TryGetTypeIDListToLoad](M_Tessa_Platform_Initialization_InitializationExtensions_TryGetTypeIDListToLoad.htm)|
Возвращает список идентификаторов типов карточек, которые должны загружаться
при инициализации, или null, если подходящих типов нет.  
[WhenClientInitializationFunc](M_Tessa_Platform_Initialization_InitializationExtensions_WhenClientInitializationFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IClientInitializationExtension](T_Tessa_Platform_Initialization_IClientInitializationExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
[WhenServerInitializationFunc](M_Tessa_Platform_Initialization_InitializationExtensions_WhenServerInitializationFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IServerInitializationExtension](T_Tessa_Platform_Initialization_IServerInitializationExtension.htm)
в соответствии с функцией isAllowedFunc, которая проверяет контекст
расширений. Если зарегистрировано несколько политик, то должны выполняться все
из них.  
## __Поля
[ConfigurationInfoKey](F_Tessa_Platform_Initialization_InitializationExtensions_ConfigurationInfoKey.htm)|
Строковый ключ, по которому расположена сериализованная информация по
конфигурации в InitializationResponse.Info. Не рекомендуется использовать
непосредственно, вместо этого используйте методы
[SetConfigurationInfo(InitializationResponse,
IConfigurationInfo)](M_Tessa_Platform_Initialization_InitializationExtensions_SetConfigurationInfo.htm)
и
[TryGetConfigurationInfo(InitializationResponse)](M_Tessa_Platform_Initialization_InitializationExtensions_TryGetConfigurationInfo.htm).  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Initialization - пространство
имён](N_Tessa_Platform_Initialization.htm)
