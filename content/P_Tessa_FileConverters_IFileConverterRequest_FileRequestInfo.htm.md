# IFileConverterRequest.FileRequestInfo - свойство
Дополнительная информация, передаваемая в запрос на конвертацию
CardGetFileContentRequest.Info. От такой информации зависит вычисление хеша
запроса (и идентификация похожих операций). Если от некоторой части этих
данных должен зависеть хеш запроса, то скопируйте их в свойство Parameters.
Значение необязательно для заполнения, его можно использовать для конвертации
виртуальных файлов.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ISerializableObject FileRequestInfo { get; }
VB __Копировать
     ReadOnly Property FileRequestInfo As ISerializableObject
    	Get
C++ __Копировать
    property ISerializableObject^ FileRequestInfo {
    	ISerializableObject^ get ();
    }
F# __Копировать
     abstract FileRequestInfo : ISerializableObject with get
#### Значение свойства
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[IFileConverterRequest - ](T_Tessa_FileConverters_IFileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
