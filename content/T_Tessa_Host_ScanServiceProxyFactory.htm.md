# ScanServiceProxyFactory - делегат
Делегат фабрики создания прокси-клиента для взаимодействия с сервисом
сканирования
## __Definition
 **Пространство имён:** [Tessa.Host](N_Tessa_Host.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public delegate IScanServiceProxy ScanServiceProxyFactory(
    	[CanBeNullAttribute] string typeName = null,
    	[CanBeNullAttribute] string assemblyFileName = null
    )
VB __Копировать
    <NotNullAttribute>
    Public Delegate Function ScanServiceProxyFactory ( 
    	<CanBeNullAttribute> Optional typeName As String = Nothing,
    	<CanBeNullAttribute> Optional assemblyFileName As String = Nothing
    ) As IScanServiceProxy
C++ __Копировать
    [NotNullAttribute]
    public delegate IScanServiceProxy^ ScanServiceProxyFactory(
    	[CanBeNullAttribute] String^ typeName = nullptr, 
    	[CanBeNullAttribute] String^ assemblyFileName = nullptr
    )
F# __Копировать
     [<NotNullAttribute>]
    type ScanServiceProxyFactory = 
        delegate of 
            [<CanBeNullAttribute>] ?typeName : string * 
            [<CanBeNullAttribute>] ?assemblyFileName : string 
    (* Defaults:
            let _typeName = defaultArg typeName null
            let _assemblyFileName = defaultArg assemblyFileName null
    *)
    -> IScanServiceProxy
#### Параметры
typeName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
    Имя типа данных или null для использования сервиса по умолчанию
assemblyFileName
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
     Имя сборки или null в которой будет осуществляться поиск сервиса сканирования или null для использования сборок по умолчанию 
#### Возвращаемое значение
[IScanServiceProxy](T_Tessa_Host_IScanServiceProxy.htm)  
Прокси-сервис
##  __См. также
#### Ссылки
[Tessa.Host - пространство имён](N_Tessa_Host.htm)
