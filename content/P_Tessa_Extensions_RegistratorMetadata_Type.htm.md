# RegistratorMetadata.Type - свойство
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
     public SessionType Type { get; }
VB __Копировать
     Public ReadOnly Property Type As SessionType
    	Get
C++ __Копировать
     public:
    virtual property SessionType Type {
    	SessionType get () sealed;
    }
F# __Копировать
     abstract Type : SessionType with get
    override Type : SessionType with get
#### Значение свойства
[SessionType](T_Tessa_Platform_Runtime_SessionType.htm)
#### Реализации
[IRegistratorMetadata.Type](P_Tessa_Extensions_IRegistratorMetadata_Type.htm)  
##  __См. также
#### Ссылки
[RegistratorMetadata - ](T_Tessa_Extensions_RegistratorMetadata.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
