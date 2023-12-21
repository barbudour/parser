# CardMetadataHelper.CoerceBeforeSaving - метод
Корректирует при необходимости значение перед сохранением в базу данных в
соответствии с заданным типом
[CardMetadataType](T_Tessa_Cards_Metadata_CardMetadataType.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Object CoerceBeforeSaving(
    	Object value,
    	CardMetadataType metadataType,
    	string fieldName = null,
    	string sectionName = null
    )
VB __Копировать
     Public Shared Function CoerceBeforeSaving ( 
    	value As Object,
    	metadataType As CardMetadataType,
    	Optional fieldName As String = Nothing,
    	Optional sectionName As String = Nothing
    ) As Object
C++ __Копировать
     public:
    static Object^ CoerceBeforeSaving(
    	Object^ value, 
    	CardMetadataType^ metadataType, 
    	String^ fieldName = nullptr, 
    	String^ sectionName = nullptr
    )
F# __Копировать
     static member CoerceBeforeSaving : 
            value : Object * 
            metadataType : CardMetadataType * 
            ?fieldName : string * 
            ?sectionName : string 
    (* Defaults:
            let _fieldName = defaultArg fieldName null
            let _sectionName = defaultArg sectionName null
    *)
    -> Object 
#### Параметры
value [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Значение, сохраняемое в базу данных.
metadataType [CardMetadataType](T_Tessa_Cards_Metadata_CardMetadataType.htm)
    Тип сохраняемого значения, определяющий представление данных в карточке.
fieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
    Имя поля, содержащее сохраняемое значение, для вывода в исключениях, или null, если имя не указано.
sectionName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
    Имя секции, содержащей сохраняемое значение, для вывода в исключениях, или null, если имя не указано.
#### Возвращаемое значение
[Object](https://learn.microsoft.com/dotnet/api/system.object)  
Скорректированное значение или исходное значение, если корректировка не
требуется.
##  __Заметки
Метод не выполняет валидацию значения на факт того, что оно соответствует
типу.
## __См. также
#### Ссылки
[CardMetadataHelper - ](T_Tessa_Cards_Metadata_CardMetadataHelper.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
