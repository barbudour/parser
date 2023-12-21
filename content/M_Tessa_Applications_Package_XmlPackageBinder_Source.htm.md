# XmlPackageBinder.Source - метод
Устанавливает в качестве источника пакета приложения хранилище storage
содержащий описание пакета
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public XmlPackageBinder Source(
    	[NotNullAttribute] IStorage storage
    )
VB __Копировать
    <NotNullAttribute>
    Public Function Source ( 
    	<NotNullAttribute> storage As IStorage
    ) As XmlPackageBinder
C++ __Копировать
     public:
    [NotNullAttribute]
    XmlPackageBinder^ Source(
    	[NotNullAttribute] IStorage^ storage
    )
F# __Копировать
     [<NotNullAttribute>]
    member Source : 
            [<NotNullAttribute>] storage : IStorage -> XmlPackageBinder 
#### Параметры
storage [IStorage](T_Tessa_Applications_Containers_Storage_IStorage.htm)
     Хранилище содержащее пакет приложения 
#### Возвращаемое значение
[XmlPackageBinder](T_Tessa_Applications_Package_XmlPackageBinder.htm)  
Ссылку на себя
## __См. также
#### Ссылки
[XmlPackageBinder - ](T_Tessa_Applications_Package_XmlPackageBinder.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
