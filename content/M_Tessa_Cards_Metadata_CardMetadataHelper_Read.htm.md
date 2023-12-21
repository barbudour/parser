# CardMetadataHelper.Read - метод
Выполняет чтение объекта заданного типа данных из байтового потока. Объект
должен был быть записан в байтовый поток посредством метода
[Write(BinaryWriter, Object, CardMetadataType,
Nullable<Boolean>)](M_Tessa_Cards_Metadata_CardMetadataHelper_Write.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Object Read(
    	BinaryReader reader,
    	CardMetadataType metadataType,
    	bool? isNullableOverride = null
    )
VB __Копировать
     Public Shared Function Read ( 
    	reader As BinaryReader,
    	metadataType As CardMetadataType,
    	Optional isNullableOverride As Boolean? = Nothing
    ) As Object
C++ __Копировать
     public:
    static Object^ Read(
    	BinaryReader^ reader, 
    	CardMetadataType^ metadataType, 
    	Nullable<bool> isNullableOverride = nullptr
    )
F# __Копировать
     static member Read : 
            reader : BinaryReader * 
            metadataType : CardMetadataType * 
            ?isNullableOverride : Nullable<bool> 
    (* Defaults:
            let _isNullableOverride = defaultArg isNullableOverride null
    *)
    -> Object 
#### Параметры
reader
[BinaryReader](https://learn.microsoft.com/dotnet/api/system.io.binaryreader)
    Объект, выполняющий чтение из байтового потока.
metadataType [CardMetadataType](T_Tessa_Cards_Metadata_CardMetadataType.htm)
    Тип записанного в байтовый поток объекта.
isNullableOverride
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
(Optional)
     Допустимость значения null в типе metadataType или null, если используется собственное значение типа значение [IsNullable](P_Tessa_Cards_Metadata_CardMetadataType_IsNullable.htm). 
#### Возвращаемое значение
[Object](https://learn.microsoft.com/dotnet/api/system.object)  
Прочитанное из байтового потока значение.
##  __См. также
#### Ссылки
[CardMetadataHelper - ](T_Tessa_Cards_Metadata_CardMetadataHelper.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
