# CardMetadataHelper.CoerceAfterLoading(Object, SchemeDbType) - метод
Корректирует при необходимости загруженное из базы данных значение в
соответствии с заданным типом
[SchemeDbType](T_Tessa_Platform_Data_SchemeDbType.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Object CoerceAfterLoading(
    	Object value,
    	SchemeDbType type
    )
VB __Копировать
     Public Shared Function CoerceAfterLoading ( 
    	value As Object,
    	type As SchemeDbType
    ) As Object
C++ __Копировать
     public:
    static Object^ CoerceAfterLoading(
    	Object^ value, 
    	SchemeDbType type
    )
F# __Копировать
     static member CoerceAfterLoading : 
            value : Object * 
            type : SchemeDbType -> Object 
#### Параметры
value [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Значение, загруженное из базы данных.
type [SchemeDbType](T_Tessa_Platform_Data_SchemeDbType.htm)
    Тип загруженного значения.
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
[CoerceAfterLoading -
перегрузка](Overload_Tessa_Cards_Metadata_CardMetadataHelper_CoerceAfterLoading.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
