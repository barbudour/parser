# StreamApplicationPackageFileEnumerator - конструктор
Initializes a new instance of the
[StreamApplicationPackageFileEnumerator](T_Tessa_Applications_Synchronization_StreamApplicationPackageFileEnumerator.htm)
class. Initializes a new instance of the
[Object](https://learn.microsoft.com/dotnet/api/system.object) class.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public StreamApplicationPackageFileEnumerator(
    	[NotNullAttribute] Func<CancellationToken, ValueTask<ApplicationPackage>> getPackageFuncAsync,
    	[NotNullAttribute] Stream stream,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> getPackageFuncAsync As Func(Of CancellationToken, ValueTask(Of ApplicationPackage)),
    	<NotNullAttribute> stream As Stream,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    StreamApplicationPackageFileEnumerator(
    	[NotNullAttribute] Func<CancellationToken, ValueTask<ApplicationPackage^>>^ getPackageFuncAsync, 
    	[NotNullAttribute] Stream^ stream, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] getPackageFuncAsync : Func<CancellationToken, ValueTask<ApplicationPackage>> * 
            [<NotNullAttribute>] stream : Stream * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> StreamApplicationPackageFileEnumerator
#### Параметры
getPackageFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ApplicationPackage](T_Tessa_Applications_Package_ApplicationPackage.htm)>>
     Пакет приложения. 
stream [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
     Поток содержащий последовательность байт файлов содержащихся в пакете находящихся в состоянии [Inserted](T_Tessa_Applications_Package_PackageFileState.htm) или [Replaced](T_Tessa_Applications_Package_PackageFileState.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
##  __См. также
#### Ссылки
[StreamApplicationPackageFileEnumerator -
](T_Tessa_Applications_Synchronization_StreamApplicationPackageFileEnumerator.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
