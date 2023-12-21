# ReadFromStreamInitializationActionAsync - делегат
Метод, выполняющий чтение из потока инициализации. Метод может освобождать
переданный ему поток.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate Task ReadFromStreamInitializationActionAsync(
    	IClientInitializationExtensionContext context,
    	Stream stream
    )
VB __Копировать
     Public Delegate Function ReadFromStreamInitializationActionAsync ( 
    	context As IClientInitializationExtensionContext,
    	stream As Stream
    ) As Task
C++ __Копировать
     public delegate Task^ ReadFromStreamInitializationActionAsync(
    	IClientInitializationExtensionContext^ context, 
    	Stream^ stream
    )
F# __Копировать
     type ReadFromStreamInitializationActionAsync = 
        delegate of 
            context : IClientInitializationExtensionContext * 
            stream : Stream -> Task
#### Параметры
context
[IClientInitializationExtensionContext](T_Tessa_Platform_Initialization_IClientInitializationExtensionContext.htm)
    Контекст инициализации.
stream [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
    Поток, из которого выполняется чтение.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[Tessa.Platform.Initialization - пространство
имён](N_Tessa_Platform_Initialization.htm)
