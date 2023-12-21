# CardMetadataHelper.ConvertToSchemeType - метод
Возвращает объект [SchemeType](T_Tessa_Scheme_SchemeType.htm), который может
разместить данные указанного объекта
[CardMetadataType](T_Tessa_Cards_Metadata_CardMetadataType.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static SchemeType ConvertToSchemeType(
    	CardMetadataType metadataType
    )
VB __Копировать
     Public Shared Function ConvertToSchemeType ( 
    	metadataType As CardMetadataType
    ) As SchemeType
C++ __Копировать
     public:
    static SchemeType^ ConvertToSchemeType(
    	CardMetadataType^ metadataType
    )
F# __Копировать
     static member ConvertToSchemeType : 
            metadataType : CardMetadataType -> SchemeType 
#### Параметры
metadataType [CardMetadataType](T_Tessa_Cards_Metadata_CardMetadataType.htm)
     Тип объекта, который требуется привести к [SchemeType](T_Tessa_Scheme_SchemeType.htm). 
#### Возвращаемое значение
[SchemeType](T_Tessa_Scheme_SchemeType.htm)  
Объект [SchemeType](T_Tessa_Scheme_SchemeType.htm), содержащий информацию о
типе, полученную для текущего объекта.
## __Заметки
По типу данных в карточке невозможно воссоздать точный тип данных в схеме.
## __Исключения
[InvalidCastException](https://learn.microsoft.com/dotnet/api/system.invalidcastexception)|
Невозможно выполнить преобразование типа объекта, т.к. он повреждён.  
---|---  
##  __См. также
#### Ссылки
[CardMetadataHelper - ](T_Tessa_Cards_Metadata_CardMetadataHelper.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
