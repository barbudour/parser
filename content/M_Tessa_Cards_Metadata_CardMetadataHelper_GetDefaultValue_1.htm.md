# CardMetadataHelper.GetDefaultValue(SchemeDbType, Boolean) - метод
Возвращает значение по умолчанию для сохранения в карточке, доступное для
заданного типа [SchemeDbType](T_Tessa_Platform_Data_SchemeDbType.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Object GetDefaultValue(
    	SchemeDbType type,
    	bool isNullable
    )
VB __Копировать
     Public Shared Function GetDefaultValue ( 
    	type As SchemeDbType,
    	isNullable As Boolean
    ) As Object
C++ __Копировать
     public:
    static Object^ GetDefaultValue(
    	SchemeDbType type, 
    	bool isNullable
    )
F# __Копировать
     static member GetDefaultValue : 
            type : SchemeDbType * 
            isNullable : bool -> Object 
#### Параметры
type [SchemeDbType](T_Tessa_Platform_Data_SchemeDbType.htm)
    Тип, для которого требуется вернуть значение по умолчанию.
isNullable [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Признак того, что тип допускает значения null.
#### Возвращаемое значение
[Object](https://learn.microsoft.com/dotnet/api/system.object)  
Значение по умолчанию для хранения в карточке, доступное для типа
[SchemeDbType](T_Tessa_Platform_Data_SchemeDbType.htm).
## __См. также
#### Ссылки
[CardMetadataHelper - ](T_Tessa_Cards_Metadata_CardMetadataHelper.htm)
[GetDefaultValue -
перегрузка](Overload_Tessa_Cards_Metadata_CardMetadataHelper_GetDefaultValue.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
