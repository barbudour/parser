# IFileConverterRequest.CardTypeID - свойство
Идентификатор типа карточки с преобразуемым файлом, который указывается в
запросе на конвертацию CardGetFileContentRequest.CardTypeID, или null, если
свойство не указывается в запросе. От значения этого свойства не зависит
вычисление хеша запроса (и идентификация похожих операций). Значение
необязательно для заполнения, его можно использовать для конвертации
виртуальных файлов.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    Guid? CardTypeID { get; set; }
VB __Копировать
     Property CardTypeID As Guid?
    	Get
    	Set
C++ __Копировать
    property Nullable<Guid> CardTypeID {
    	Nullable<Guid> get ();
    	void set (Nullable<Guid> value);
    }
F# __Копировать
     abstract CardTypeID : Nullable<Guid> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[IFileConverterRequest - ](T_Tessa_FileConverters_IFileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
[Tessa.Platform.ObjectSealedException]
