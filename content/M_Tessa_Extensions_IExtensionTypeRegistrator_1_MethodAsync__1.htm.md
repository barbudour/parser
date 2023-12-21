# IExtensionTypeRegistrator<TExtension>.MethodAsync<TContext> \- метод
Регистрирует метод, который можно асинхронно выполнить для текущего типа
расширения.
##  __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     IExtensionTypeRegistrator<TExtension> MethodAsync<TContext>(
    	Expression<ExtensionMethodReferenceAsync<TExtension, TContext>> method
    )
    where TContext : class, IExtensionContext
VB __Копировать
     Function MethodAsync(Of TContext As {Class, IExtensionContext}) ( 
    	method As Expression(Of ExtensionMethodReferenceAsync(Of TExtension, TContext))
    ) As IExtensionTypeRegistrator(Of TExtension)
C++ __Копировать
    generic<typename TContext>
    where TContext : ref class, IExtensionContext
    IExtensionTypeRegistrator<TExtension>^ MethodAsync(
    	Expression<ExtensionMethodReferenceAsync<TExtension, TContext>^>^ method
    )
F# __Копировать
     abstract MethodAsync : 
            method : Expression<ExtensionMethodReferenceAsync<'TExtension, 'TContext>> -> IExtensionTypeRegistrator<'TExtension>  when 'TContext : not struct and IExtensionContext
#### Параметры
method
[Expression](https://learn.microsoft.com/dotnet/api/system.linq.expressions.expression-1)<[ExtensionMethodReferenceAsync](T_Tessa_Extensions_ExtensionMethodReferenceAsync_2.htm)<[TExtension](T_Tessa_Extensions_IExtensionTypeRegistrator_1.htm),
TContext>>
    Делегат, возвращающий метод, который можно асинхронно выполнить для текущего типа расширения.
#### Параметры типа
TContext
     Тип параметра для заданного метода, реализующий интерфейс [IExtensionContext]. 
#### Возвращаемое значение
[IExtensionTypeRegistrator](T_Tessa_Extensions_IExtensionTypeRegistrator_1.htm)<[TExtension](T_Tessa_Extensions_IExtensionTypeRegistrator_1.htm)>  
Текущий объект для цепочки вызовов.
##  __См. также
#### Ссылки
[IExtensionTypeRegistrator<TExtension> \-
](T_Tessa_Extensions_IExtensionTypeRegistrator_1.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
