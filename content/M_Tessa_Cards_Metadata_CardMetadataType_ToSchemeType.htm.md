# CardMetadataType.ToSchemeType - метод
Возвращает объект [SchemeType](T_Tessa_Scheme_SchemeType.htm), содержащий
информацию о типе, полученную для текущего объекта.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SchemeType ToSchemeType()
VB __Копировать
     Public Function ToSchemeType As SchemeType
C++ __Копировать
     public:
    SchemeType^ ToSchemeType()
F# __Копировать
     member ToSchemeType : unit -> SchemeType 
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
[CardMetadataType - ](T_Tessa_Cards_Metadata_CardMetadataType.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
