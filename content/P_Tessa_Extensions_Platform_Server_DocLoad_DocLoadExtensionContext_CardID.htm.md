# DocLoadExtensionContext.CardID - свойство
Идентификатор карточки, найденный расширением по штрих-коду, указанному в
контексте. Расширение должно установить идентификатор в этом свойстве.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.DocLoad](N_Tessa_Extensions_Platform_Server_DocLoad.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid? CardID { get; set; }
VB __Копировать
     Public Property CardID As Guid?
    	Get
    	Set
C++ __Копировать
     public:
    virtual property Nullable<Guid> CardID {
    	Nullable<Guid> get () sealed;
    	void set (Nullable<Guid> value) sealed;
    }
F# __Копировать
     abstract CardID : Nullable<Guid> with get, set
    override CardID : Nullable<Guid> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
#### Реализации
[IDocLoadExtensionContext.CardID](P_Tessa_Extensions_Platform_Server_DocLoad_IDocLoadExtensionContext_CardID.htm)  
##  __См. также
#### Ссылки
[DocLoadExtensionContext -
](T_Tessa_Extensions_Platform_Server_DocLoad_DocLoadExtensionContext.htm)
[Tessa.Extensions.Platform.Server.DocLoad - пространство
имён](N_Tessa_Extensions_Platform_Server_DocLoad.htm)
