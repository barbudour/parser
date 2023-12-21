# ExtensionMethodAsync<TContext> \- делегат
Метод, который можно асинхронно выполнить в расширении.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate Task ExtensionMethodAsync<in TContext>(
    	TContext context
    )
    where TContext : class, IExtensionContext
VB __Копировать
     Public Delegate Function ExtensionMethodAsync(Of In TContext As {Class, IExtensionContext}) ( 
    	context As TContext
    ) As Task
C++ __Копировать
    generic<typename TContext>
    where TContext : ref class, IExtensionContext
    public delegate Task^ ExtensionMethodAsync(
    	TContext context
    )
F# __Копировать
     type ExtensionMethodAsync = 
        delegate of 
            context : 'TContext -> Task
#### Параметры
context TContext
    Параметр выполняемого метода.
#### Параметры типа
TContext
    Тип параметра для выполняемого метода.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
