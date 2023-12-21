# ApplicationPackageFileContent - конструктор
Инициализирует новый экземпляр класса
[ApplicationPackageFileContent](T_Tessa_Applications_Package_ApplicationPackageFileContent.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationPackageFileContent(
    	ApplicationPackageFile file,
    	Func<CancellationToken, ValueTask<Stream>> getFileContentAsync,
    	Func<CancellationToken, ValueTask<long>> getFileSizeAsync
    )
VB __Копировать
     Public Sub New ( 
    	file As ApplicationPackageFile,
    	getFileContentAsync As Func(Of CancellationToken, ValueTask(Of Stream)),
    	getFileSizeAsync As Func(Of CancellationToken, ValueTask(Of Long))
    )
C++ __Копировать
     public:
    ApplicationPackageFileContent(
    	ApplicationPackageFile^ file, 
    	Func<CancellationToken, ValueTask<Stream^>>^ getFileContentAsync, 
    	Func<CancellationToken, ValueTask<long long>>^ getFileSizeAsync
    )
F# __Копировать
     new : 
            file : ApplicationPackageFile * 
            getFileContentAsync : Func<CancellationToken, ValueTask<Stream>> * 
            getFileSizeAsync : Func<CancellationToken, ValueTask<int64>> -> ApplicationPackageFileContent
#### Параметры
file
[ApplicationPackageFile](T_Tessa_Applications_Package_ApplicationPackageFile.htm)
getFileContentAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>>
getFileSizeAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>>
## __См. также
#### Ссылки
[ApplicationPackageFileContent -
](T_Tessa_Applications_Package_ApplicationPackageFileContent.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
