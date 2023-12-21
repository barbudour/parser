# GenericExtensions.Execute<TContext> \- метод
Вызывает выполнение действия action, если доступен контекст context
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void Execute<TContext>(
    	[CanBeNullAttribute] this TContext context,
    	[NotNullAttribute] Action<TContext> action
    )
    where TContext : class
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub Execute(Of TContext As Class) ( 
    	<CanBeNullAttribute> context As TContext,
    	<NotNullAttribute> action As Action(Of TContext)
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    generic<typename TContext>
    where TContext : ref class
    static void Execute(
    	[CanBeNullAttribute] TContext context, 
    	[NotNullAttribute] Action<TContext>^ action
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member Execute : 
            [<CanBeNullAttribute>] context : 'TContext * 
            [<NotNullAttribute>] action : Action<'TContext> -> unit  when 'TContext : not struct
#### Параметры
context TContext
     Контекст выполнения 
action
[Action](https://learn.microsoft.com/dotnet/api/system.action-1)<TContext>
     Выполняемое действие 
#### Параметры типа
TContext
     Тип контекста 
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
