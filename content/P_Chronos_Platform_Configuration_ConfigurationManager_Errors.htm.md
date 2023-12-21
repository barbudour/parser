# ConfigurationManager.Errors - свойство
Ошибки, которые возникли при разборе файлов конфигурации сервера.
##  __Definition
 **Пространство имён:**
[Chronos.Platform.Configuration](N_Chronos_Platform_Configuration.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public ReadOnlyCollection<ConfigurationError> Errors { get; }
VB __Копировать
     Public ReadOnly Property Errors As ReadOnlyCollection(Of ConfigurationError)
    	Get
C++ __Копировать
     public:
    virtual property ReadOnlyCollection<ConfigurationError^>^ Errors {
    	ReadOnlyCollection<ConfigurationError^>^ get () sealed;
    }
F# __Копировать
     abstract Errors : ReadOnlyCollection<ConfigurationError> with get
    override Errors : ReadOnlyCollection<ConfigurationError> with get
#### Значение свойства
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[ConfigurationError](T_Chronos_Platform_Configuration_ConfigurationError.htm)>
#### Реализации
[IConfigurationManager.Errors](P_Chronos_Platform_Configuration_IConfigurationManager_Errors.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[ConfigurationManager -
](T_Chronos_Platform_Configuration_ConfigurationManager.htm)
[Chronos.Platform.Configuration - пространство
имён](N_Chronos_Platform_Configuration.htm)
