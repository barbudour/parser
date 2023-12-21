# IExtensionPolicyContainer.Register - метод
Регистрирует заданную политику, которую можно будет получить по всем типам её
интерфейсов, кроме [Tessa.Extensions.IExtensionPolicy].
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     IExtensionPolicyContainer Register(
    	IExtensionPolicy policy,
    	bool append = false
    )
VB __Копировать
     Function Register ( 
    	policy As IExtensionPolicy,
    	Optional append As Boolean = false
    ) As IExtensionPolicyContainer
C++ __Копировать
    IExtensionPolicyContainer^ Register(
    	IExtensionPolicy^ policy, 
    	bool append = false
    )
F# __Копировать
     abstract Register : 
            policy : IExtensionPolicy * 
            ?append : bool 
    (* Defaults:
            let _append = defaultArg append false
    *)
    -> IExtensionPolicyContainer 
#### Параметры
policy [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
    Регистрируемая политика.
append [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что политика допускает несколько экземпляров и будет добавлена к списку вместо перезаписи.
#### Возвращаемое значение
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)  
Контейнер для цепочки вызовов.
##  __См. также
#### Ссылки
[IExtensionPolicyContainer -
](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
