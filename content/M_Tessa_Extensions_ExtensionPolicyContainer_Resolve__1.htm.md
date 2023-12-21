# ExtensionPolicyContainer.Resolve<TPolicy> \- метод
Возвращает политику заданного типа, зарегистрированную в контейнере. Если для
типа зарегистрировано несколько политик, то возвращается последняя.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public TPolicy Resolve<TPolicy>()
    where TPolicy : class, IExtensionPolicy
VB __Копировать
     Public Function Resolve(Of TPolicy As {Class, IExtensionPolicy}) As TPolicy
C++ __Копировать
     public:
    generic<typename TPolicy>
    where TPolicy : ref class, IExtensionPolicy
    virtual TPolicy Resolve() sealed
F# __Копировать
     abstract Resolve : unit -> 'TPolicy  when 'TPolicy : not struct and IExtensionPolicy
    override Resolve : unit -> 'TPolicy  when 'TPolicy : not struct and IExtensionPolicy
#### Параметры типа
TPolicy
    Тип интерфейса возвращаемой политики.
#### Возвращаемое значение
TPolicy  
Политика заданого типа, зарегистрированная в контейнере.
#### Реализации
[IExtensionPolicyContainer.Resolve<TPolicy>()](M_Tessa_Extensions_IExtensionPolicyContainer_Resolve__1.htm)  
##  __См. также
#### Ссылки
[ExtensionPolicyContainer - ](T_Tessa_Extensions_ExtensionPolicyContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
