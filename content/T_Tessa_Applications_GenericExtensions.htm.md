# GenericExtensions - класс
The generic extensions.
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class GenericExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class GenericExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class GenericExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type GenericExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ GenericExtensions
##  __Методы
[Execute<TContext>](M_Tessa_Applications_GenericExtensions_Execute__1.htm)|
Вызывает выполнение действия action, если доступен контекст context  
---|---  
[IfFalse](M_Tessa_Applications_GenericExtensions_IfFalse.htm)|  Выполняет
action если conditional равен false  
[IfTrue](M_Tessa_Applications_GenericExtensions_IfTrue.htm)|  Выполняет action
если conditional равен true  
[OnNullThrow<TValue,
TException>](M_Tessa_Applications_GenericExtensions_OnNullThrow__2.htm)|
Возвращает значение параметра value, если он не равен null, в противном случае
вызывает исключение exception  
[With<TContext, TResult>](M_Tessa_Applications_GenericExtensions_With__2.htm)|
Используется для разыменовывания ссылок.  
## __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
