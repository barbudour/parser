# IRegistratorMetadata.Type - свойство
Тип сессии, для которой будет выполняться регистратор, или
[Tessa.Platform.Runtime.SessionType.Unknown], если регистратор выполняется для
любого типа сессии и на клиенте, и на сервере (по умолчанию). Значение,
отличное от [Tessa.Platform.Runtime.SessionType.Unknown], актуально только для
сборок, которые могут сканироваться на наличие регистраторов и на клиенте, и
на сервере.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [DefaultValueAttribute(SessionType.Unknown)]
    SessionType Type { get; }
VB __Копировать
    <DefaultValueAttribute(SessionType.Unknown)>
    ReadOnly Property Type As SessionType
    	Get
C++ __Копировать
    [DefaultValueAttribute(SessionType::Unknown)]
    property SessionType Type {
    	SessionType get ();
    }
F# __Копировать
     [<DefaultValueAttribute(SessionType.Unknown)>]
    abstract Type : SessionType with get
#### Значение свойства
[SessionType](T_Tessa_Platform_Runtime_SessionType.htm)
##  __См. также
#### Ссылки
[IRegistratorMetadata - ](T_Tessa_Extensions_IRegistratorMetadata.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
