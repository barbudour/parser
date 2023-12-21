# IFileConverterRequest.VersionID - свойство
Идентификатор версии преобразуемого файла. Значение используется для
вычисления хеша запроса.
##  __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    Guid VersionID { get; set; }
VB __Копировать
     Property VersionID As Guid
    	Get
    	Set
C++ __Копировать
    property Guid VersionID {
    	Guid get ();
    	void set (Guid value);
    }
F# __Копировать
     abstract VersionID : Guid with get, set
#### Значение свойства
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[IFileConverterRequest - ](T_Tessa_FileConverters_IFileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
[Tessa.Platform.ObjectSealedException]
