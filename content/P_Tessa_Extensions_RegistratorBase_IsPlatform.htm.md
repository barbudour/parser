# RegistratorBase.IsPlatform - свойство
Признак того, что объект выполняет регистрацию платформенных расширений. Этот
признак используется системой, не рекомендуется его устанавливать.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsPlatform { get; set; }
VB __Копировать
     Public Property IsPlatform As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    virtual property bool IsPlatform {
    	bool get () sealed;
    	void set (bool value) sealed;
    }
F# __Копировать
     abstract IsPlatform : bool with get, set
    override IsPlatform : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Реализации
[IRegistrator.IsPlatform](P_Tessa_Extensions_IRegistrator_IsPlatform.htm)  
##  __См. также
#### Ссылки
[RegistratorBase - ](T_Tessa_Extensions_RegistratorBase.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
