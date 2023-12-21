# CardMetadataHelper.Write - метод
Выполняет запись объекта заданного типа данных в байтовый поток. Объект может
быть прочитан из байтового потока посредством метода [Read(BinaryReader,
CardMetadataType,
Nullable<Boolean>)](M_Tessa_Cards_Metadata_CardMetadataHelper_Read.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void Write(
    	BinaryWriter writer,
    	Object value,
    	CardMetadataType metadataType,
    	bool? isNullableOverride = null
    )
VB __Копировать
     Public Shared Sub Write ( 
    	writer As BinaryWriter,
    	value As Object,
    	metadataType As CardMetadataType,
    	Optional isNullableOverride As Boolean? = Nothing
    )
C++ __Копировать
     public:
    static void Write(
    	BinaryWriter^ writer, 
    	Object^ value, 
    	CardMetadataType^ metadataType, 
    	Nullable<bool> isNullableOverride = nullptr
    )
F# __Копировать
     static member Write : 
            writer : BinaryWriter * 
            value : Object * 
            metadataType : CardMetadataType * 
            ?isNullableOverride : Nullable<bool> 
    (* Defaults:
            let _isNullableOverride = defaultArg isNullableOverride null
    *)
    -> unit 
#### Параметры
writer
[BinaryWriter](https://learn.microsoft.com/dotnet/api/system.io.binarywriter)
    Объект, осуществляющий запись в байтовый поток
value [Object](https://learn.microsoft.com/dotnet/api/system.object)
     Значение, которое требуется записать в байтовый поток. Если значение равно null, а тип metadataType не допускает значений null, то возвращается значение по умолчанию для этого типа.
metadataType [CardMetadataType](T_Tessa_Cards_Metadata_CardMetadataType.htm)
    Тип объекта, который требуется записать в байтовый поток.
isNullableOverride
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
(Optional)
     Допустимость значения null в типе metadataType или null, если используется собственное значение типа значение [IsNullable](P_Tessa_Cards_Metadata_CardMetadataType_IsNullable.htm). 
## __См. также
#### Ссылки
[CardMetadataHelper - ](T_Tessa_Cards_Metadata_CardMetadataHelper.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
