# RegistratorBase.UnityContainer - свойство
Контейнер Unity, в котором выполняется регистрация. Гарантированно не равен
null.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IUnityContainer UnityContainer { get; set; }
VB __Копировать
     Public Property UnityContainer As IUnityContainer
    	Get
    	Set
C++ __Копировать
     public:
    virtual property IUnityContainer^ UnityContainer {
    	IUnityContainer^ get () sealed;
    	void set (IUnityContainer^ value) sealed;
    }
F# __Копировать
     abstract UnityContainer : IUnityContainer with get, set
    override UnityContainer : IUnityContainer with get, set
#### Значение свойства
IUnityContainer
#### Реализации
[IRegistrator.UnityContainer](P_Tessa_Extensions_IRegistrator_UnityContainer.htm)  
##  __См. также
#### Ссылки
[RegistratorBase - ](T_Tessa_Extensions_RegistratorBase.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
