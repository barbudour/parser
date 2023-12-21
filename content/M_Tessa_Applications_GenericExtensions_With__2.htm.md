# GenericExtensions.With<TContext, TResult> \- метод
Используется для разыменовывания ссылок.
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [CanBeNullAttribute]
    public static TResult With<TContext, TResult>(
    	[CanBeNullAttribute] this TContext callSite,
    	[NotNullAttribute] Func<TContext, TResult> selector
    )
    where TContext : class
VB __Копировать
    <ExtensionAttribute>
    <CanBeNullAttribute>
    Public Shared Function With(Of TContext As Class, TResult) ( 
    	<CanBeNullAttribute> callSite As TContext,
    	<NotNullAttribute> selector As Func(Of TContext, TResult)
    ) As TResult
C++ __Копировать
     public:
    [ExtensionAttribute]
    [CanBeNullAttribute]
    generic<typename TContext, typename TResult>
    where TContext : ref class
    static TResult With(
    	[CanBeNullAttribute] TContext callSite, 
    	[NotNullAttribute] Func<TContext, TResult>^ selector
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<CanBeNullAttribute>]
    static member With : 
            [<CanBeNullAttribute>] callSite : 'TContext * 
            [<NotNullAttribute>] selector : Func<'TContext, 'TResult> -> 'TResult  when 'TContext : not struct
#### Параметры
callSite TContext
     Объект для которого вызывается разыменование 
selector
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<TContext,
TResult>
     Функция выполняющая разыменование 
#### Параметры типа
TContext
     Тип обрабатываемого элемента 
TResult
     Тип результата разыменования 
#### Возвращаемое значение
TResult  
Результат разыменования или null, если разыменовываемый объект равен null
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа TContext. При вызове метода для экземпляра следует опускать
первый параметр. Дополнительные сведения см. в разделе [Методы расширения
(Visual Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[GenericExtensions - ](T_Tessa_Applications_GenericExtensions.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
