# XmlPackageBinder - конструктор
Initializes a new instance of the
[XmlPackageBinder](T_Tessa_Applications_Package_XmlPackageBinder.htm) class.
Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public XmlPackageBinder(
    	[NotNullAttribute] IStorageFactory storageFactory,
    	[NotNullAttribute] HashCalculateDelegateAsync hashCalculatorAsync,
    	[NotNullAttribute] IIgnoredFilesProvider ignoredFilesProvider
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> storageFactory As IStorageFactory,
    	<NotNullAttribute> hashCalculatorAsync As HashCalculateDelegateAsync,
    	<NotNullAttribute> ignoredFilesProvider As IIgnoredFilesProvider
    )
C++ __Копировать
     public:
    XmlPackageBinder(
    	[NotNullAttribute] IStorageFactory^ storageFactory, 
    	[NotNullAttribute] HashCalculateDelegateAsync^ hashCalculatorAsync, 
    	[NotNullAttribute] IIgnoredFilesProvider^ ignoredFilesProvider
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] storageFactory : IStorageFactory * 
            [<NotNullAttribute>] hashCalculatorAsync : HashCalculateDelegateAsync * 
            [<NotNullAttribute>] ignoredFilesProvider : IIgnoredFilesProvider -> XmlPackageBinder
#### Параметры
storageFactory
[IStorageFactory](T_Tessa_Applications_Containers_Storage_IStorageFactory.htm)
     Фабрика из которой требуется получить информацию 
hashCalculatorAsync
[HashCalculateDelegateAsync](T_Tessa_Applications_HashCalculateDelegateAsync.htm)
     Калькулятор хэша 
ignoredFilesProvider
[IIgnoredFilesProvider](T_Tessa_Applications_Package_IIgnoredFilesProvider.htm)
     The ignored Files Provider. 
## __См. также
#### Ссылки
[XmlPackageBinder - ](T_Tessa_Applications_Package_XmlPackageBinder.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
