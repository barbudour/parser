# FileConverterExtensions.RegisterWorker<T> \- метод
Выполняет регистрацию реализации
[IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm) для
конвертации файла в формат outputFormat. Рекомендуется вызывать в методе
[FinalizeRegistration()](M_Tessa_Extensions_IRegistrator_FinalizeRegistration.htm).
Если не указать параметр overwrite равным true, то метод не выполнит действий,
когда тип уже зарегистрирован (но и исключений не выбросит). Также метод не
выполняет действий, когда в контейнере container не зарегистрирована
зависимость
[IFileConverterAggregateWorker](T_Tessa_FileConverters_IFileConverterAggregateWorker.htm)
(при инициализации на сервере по умолчанию регистрация есть).
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IUnityContainer RegisterWorker<T>(
    	this IUnityContainer container,
    	FileConverterFormat outputFormat,
    	Func<IUnityContainer, T> createWorkerFunc = null,
    	bool overwrite = false
    )
    where T : IFileConverterWorker
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function RegisterWorker(Of T As IFileConverterWorker) ( 
    	container As IUnityContainer,
    	outputFormat As FileConverterFormat,
    	Optional createWorkerFunc As Func(Of IUnityContainer, T) = Nothing,
    	Optional overwrite As Boolean = false
    ) As IUnityContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    generic<typename T>
    where T : IFileConverterWorker
    static IUnityContainer^ RegisterWorker(
    	IUnityContainer^ container, 
    	FileConverterFormat outputFormat, 
    	Func<IUnityContainer^, T>^ createWorkerFunc = nullptr, 
    	bool overwrite = false
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RegisterWorker : 
            container : IUnityContainer * 
            outputFormat : FileConverterFormat * 
            ?createWorkerFunc : Func<IUnityContainer, 'T> * 
            ?overwrite : bool 
    (* Defaults:
            let _createWorkerFunc = defaultArg createWorkerFunc null
            let _overwrite = defaultArg overwrite false
    *)
    -> IUnityContainer  when 'T : IFileConverterWorker
#### Параметры
container IUnityContainer
    Контейнер Unity.
outputFormat
[FileConverterFormat](T_Tessa_FileConverters_FileConverterFormat.htm)
    Формат файла, в который выполняется конвертация.
createWorkerFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<IUnityContainer,
T> (Optional)
     Функция, выполняющая создание объекта, используя контейнер container, или null, если объект создаётся с параметрами по умолчанию средствами контейнера. 
overwrite [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что регистрация должна перезаписать уже известную регистрацию.
#### Параметры типа
T
     Тип регистрируемого объекта, который реализует интерфейс [IFileConverterWorker](T_Tessa_FileConverters_IFileConverterWorker.htm). 
#### Возвращаемое значение
IUnityContainer  
Контейнер Unity container для цепочки вызовов.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа IUnityContainer. При вызове метода для экземпляра следует
опускать первый параметр. Дополнительные сведения см. в разделе [Методы
расширения (Visual Basic)](https://docs.microsoft.com/dotnet/visual-
basic/programming-guide/language-features/procedures/extension-methods) или
[Методы расширения (Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[FileConverterExtensions -
](T_Tessa_FileConverters_FileConverterExtensions.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
