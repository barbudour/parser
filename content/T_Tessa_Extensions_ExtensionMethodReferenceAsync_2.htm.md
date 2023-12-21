# ExtensionMethodReferenceAsync<TExtension, TContext> \- делегат
Делегат, возвращающий метод расширения, который можно асинхронно выполнить.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate ExtensionMethodAsync<TContext> ExtensionMethodReferenceAsync<in TExtension, in TContext>(
    	TExtension extension
    )
    where TExtension : class, IExtension
    where TContext : class, IExtensionContext
VB __Копировать
     Public Delegate Function ExtensionMethodReferenceAsync(Of In TExtension As {Class, IExtension}, In TContext As {Class, IExtensionContext}) ( 
    	extension As TExtension
    ) As ExtensionMethodAsync(Of TContext)
C++ __Копировать
    generic<typename TExtension, typename TContext>
    where TExtension : ref class, IExtension
    where TContext : ref class, IExtensionContext
    public delegate ExtensionMethodAsync<TContext>^ ExtensionMethodReferenceAsync(
    	TExtension extension
    )
F# __Копировать
     type ExtensionMethodReferenceAsync = 
        delegate of 
            extension : 'TExtension -> ExtensionMethodAsync<'TContext>
#### Параметры
extension TExtension
    Параметр метода расширения, который можно асинхронно выполнить.
#### Параметры типа
TExtension
    Тип расширения.
TContext
    Тип параметра для метода расширения, который можно асинхронно выполнить.
#### Возвращаемое значение
[ExtensionMethodAsync](T_Tessa_Extensions_ExtensionMethodAsync_1.htm)<TContext>  
Метод расширения, который можно асинхронно выполнить.
##  __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
