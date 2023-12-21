# IExtensionPolicyContainer.ResolveAll<TPolicy> \- метод
Возвращает все политики заданного типа, зарегистрированные в контейнере. Если
для типа не зарегистрировано политик, то возвращается пустое перечисление.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     IEnumerable<TPolicy> ResolveAll<TPolicy>()
    where TPolicy : class, IExtensionPolicy
VB __Копировать
     Function ResolveAll(Of TPolicy As {Class, IExtensionPolicy}) As IEnumerable(Of TPolicy)
C++ __Копировать
    generic<typename TPolicy>
    where TPolicy : ref class, IExtensionPolicy
    IEnumerable<TPolicy>^ ResolveAll()
F# __Копировать
     abstract ResolveAll : unit -> IEnumerable<'TPolicy>  when 'TPolicy : not struct and IExtensionPolicy
#### Параметры типа
TPolicy
    Тип интерфейса возвращаемых политик.
#### Возвращаемое значение
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<TPolicy>  
Все политики заданого типа, зарегистрированные в контейнере.
##  __См. также
#### Ссылки
[IExtensionPolicyContainer -
](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
