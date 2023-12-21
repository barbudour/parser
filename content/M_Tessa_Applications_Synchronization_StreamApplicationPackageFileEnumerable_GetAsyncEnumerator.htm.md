# StreamApplicationPackageFileEnumerable.GetAsyncEnumerator - метод
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IAsyncEnumerator<ApplicationPackageFileContent> GetAsyncEnumerator(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetAsyncEnumerator ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As IAsyncEnumerator(Of ApplicationPackageFileContent)
C++ __Копировать
     public:
    virtual IAsyncEnumerator<ApplicationPackageFileContent^>^ GetAsyncEnumerator(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetAsyncEnumerator : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> IAsyncEnumerator<ApplicationPackageFileContent> 
    override GetAsyncEnumerator : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> IAsyncEnumerator<ApplicationPackageFileContent> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[IAsyncEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.iasyncenumerator-1)<[ApplicationPackageFileContent](T_Tessa_Applications_Package_ApplicationPackageFileContent.htm)>
#### Реализации
[IAsyncEnumerable<T>.GetAsyncEnumerator(CancellationToken)](https://learn.microsoft.com/dotnet/api/system.collections.generic.iasyncenumerable-1.getasyncenumerator#system-
collections-generic-iasyncenumerable-1-getasyncenumerator\(system-threading-
cancellationtoken\))  
##  __См. также
#### Ссылки
[StreamApplicationPackageFileEnumerable -
](T_Tessa_Applications_Synchronization_StreamApplicationPackageFileEnumerable.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
