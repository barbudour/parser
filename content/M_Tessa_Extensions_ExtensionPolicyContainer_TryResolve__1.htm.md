# ExtensionPolicyContainer.TryResolve<TPolicy> \- метод
Возвращает политику заданного типа, зарегистрированную в контейнере, или null,
если политика не была зарегистрирована. Если для типа зарегистрировано
несколько политик, то возвращается последняя.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public TPolicy TryResolve<TPolicy>()
    where TPolicy : class, IExtensionPolicy
VB __Копировать
     Public Function TryResolve(Of TPolicy As {Class, IExtensionPolicy}) As TPolicy
C++ __Копировать
     public:
    generic<typename TPolicy>
    where TPolicy : ref class, IExtensionPolicy
    virtual TPolicy TryResolve() sealed
F# __Копировать
     abstract TryResolve : unit -> 'TPolicy  when 'TPolicy : not struct and IExtensionPolicy
    override TryResolve : unit -> 'TPolicy  when 'TPolicy : not struct and IExtensionPolicy
#### Параметры типа
TPolicy
    Тип интерфейса возвращаемой политики.
#### Возвращаемое значение
TPolicy  
Политика заданого типа, зарегистрированная в контейнере, или null, если
политика не была зарегистрирована.
#### Реализации
[IExtensionPolicyContainer.TryResolve<TPolicy>()](M_Tessa_Extensions_IExtensionPolicyContainer_TryResolve__1.htm)  
##  __См. также
#### Ссылки
[ExtensionPolicyContainer - ](T_Tessa_Extensions_ExtensionPolicyContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
